#!/usr/bin/env python3

import sys
import threading

from kafka import KafkaProducer, KafkaConsumer


should_quit = False


def read_messages(consumer):
    global curchan
    while not should_quit:
        # Subscribe to the appropriate topics
        consumer.subscribe([
            "chat_channel_{}".format(curchan) if curchan else None,
            "chat_user_{}".format(user) for user in consumer.list_topics()
        ])
        # Poll for messages
        received = consumer.poll(100)
        # Process messages
        for channel, messages in received.items():
            for msg in messages:
                if channel.topic == "chat_channel_{}".format(curchan):
                    print("< %s: %s" % (channel.topic, msg.value))
                else:
                    print("[Private message from %s]: %s" % (msg.key, msg.value))


def cmd_msg(producer, line):
    # Vérifie qu'un canal est actif
    if curchan is None:
        print("Aucun canal actif.")
        return

    # Envoie le message
    producer.send(topic="chat_channel_{}".format(curchan), value="{}: {}".format(nick, line))


def cmd_join(consumer, producer, line):
    # Vérifie que le nom du canal est valide
    if not line.startswith("#") or not line.replace("#", "").isalnum():
        print("Nom de canal invalide : %s" % line)
        return

    # Met à jour le canal actif
    global curchan
    curchan = line

    # Abonne le consommateur au canal
    consumer.subscribe([line])

    # Envoie une notification de connexion
    producer.send(topic="chat_channel_{}".format(curchan), value="{} a rejoint le canal".format(nick))


def cmd_part(consumer, producer, line):
    # Vérifie que le canal est rejoint
    if curchan != line:
        print("Vous n'êtes pas membre de ce canal.")
        return

    # Désabonne le consommateur du canal
    consumer.unsubscribe([line])

    # Envoie une notification de déconnexion
    producer.send(topic="chat_channel_{}".format(curchan), value="{} a quitté le canal".format(nick))

    # Met à jour le canal actif
    global curchan
    curchan = None


def cmd_quit(producer, line):
    # Send a quit notification
    producer.send(topic="chat_channel_{}".format(curchan), value="{} a quitté".format(nick))

    # Shut down the producer and consumer
    producer.close()
    consumer.close()

    # Indicate that the client is quitting
    global should_quit
    should_quit = True

def cmd_active(consumer, producer, line):
    # Vérifie que le canal est rejoint
    if line not in consumer.list_topics():
        print("Canal non trouvé : %s" % line)
        return

    # Met à jour le canal actif
    global curchan
    curchan = line


def main_loop(nick, consumer, producer):
    curchan = None

    while True:
        try:
            if curchan is None:
                line = input("> ")
            else:
                line = input("[%s]> " % curchan)
        except EOFError:
            print("/quit")
            line = "/quit"

        if line.startswith("/"):
            cmd, *args = line[1:].split(" ", maxsplit=1)
            cmd = cmd.lower()
            args = None if args == [] else args[0]
        else:
            cmd = "msg"
            args = line

        if cmd == "msg":
            cmd_msg(producer, curchan, args)
        elif cmd == "join":
            cmd_join(consumer, producer, args)
        elif cmd == "part":
            cmd_part(consumer, producer, args)
        elif cmd == "quit":
            cmd_quit(producer, args)
            break
        # TODO: rajouter des commandes ici



def main():
    if len(sys.argv) != 2:
        print("usage: %s nick" % sys.argv[0])
        return 1

    nick = sys.argv[1]
    consumer = KafkaConsumer()
    producer = KafkaProducer()
    th = threading.Thread(target=read_messages, args=(consumer,))
    th.start()

    try:
        main_loop(nick, consumer, producer)
    finally:
        global should_quit
        should_quit = True
        th.join()



if __name__ == "__main__":
    sys.exit(main())

# Exo 2
def cmd_join_exo2(consumer, producer, line):
    # Vérifie que le nom du canal est valide
    if not line.startswith("#") or not line.replace("#", "").isalnum():
        print("Nom de canal invalide : %s" % line)
        return

    # Met à jour le canal actif
    global curchan
    curchan = line

    # Abonne le consommateur au canal
    consumer.subscribe([line])

    # Envoie une notification de connexion
    producer.send(topic="chat_channel_{}".format(curchan), value="{} a rejoint le canal".format(nick))

def cmd_part_exo2(consumer, producer, line):
    # Vérifie que le canal est rejoint
    if curchan != line:
        print("Vous n'êtes pas membre de ce canal.")
        return

    # Désabonne le consommateur du canal
    consumer.unsubscribe([line])

    # Envoie une notification de déconnexion
    producer.send(topic="chat_channel_{}".format(curchan), value="{} a quitté le canal".format(nick))

    # Met à jour le canal actif
    global curchan
    curchan = None

def cmd_quit_exo2(producer, line):
    # Vérifie que le canal est rejoint
    if curchan is None:
        print("Aucun canal actif.")
        return

    # Envoie une notification de déconnexion
    for chan in consumer.list_topics():
        producer.send(topic="chat_channel_{}".format(chan), value="{} a quitté".format(nick))

    # Met à jour le canal actif
    global curchan
    curchan = None

    # Ferme le producteur et le consommateur
    producer.close()
    consumer.close()
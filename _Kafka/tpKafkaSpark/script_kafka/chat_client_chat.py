#!/usr/bin/env python3

import sys
import threading
from kafka import KafkaProducer, KafkaConsumer

should_quit = False


def read_messages(consumer):
    while not should_quit:
        received = consumer.poll(100)
        for channel, messages in received.items():
            for msg in messages:
                print("< %s: %s" % (channel.topic, msg.value))


def cmd_msg(producer, channel, line):
    if channel is not None:
        producer.send(channel, value=f"{nick}: {line}".encode('utf-8'))
    else:
        print("No active channel selected.")


def cmd_join(consumer, producer, line):
    channel = line.strip()
    if channel.startswith("#") and all(c.isalnum() or c == '-' for c in channel[1:]):
        consumer.subscribe([channel])
        print("Joined channel:", channel)
    else:
        print("Invalid channel name.")


def cmd_part(consumer, producer, line):
    channel = line.strip()
    if consumer.subscription() and channel in consumer.subscription():
        consumer.unsubscribe()
        print("Left channel:", channel)
    else:
        print("Channel not joined.")


def cmd_quit(producer, line):
    producer.flush()
    print("Goodbye!")


def cmd_active(curchan, line):
    channel = line.strip()
    if curchan is not None and curchan != channel:
        curchan = channel
        print("Active channel set to:", curchan)
    else:
        print("Channel not joined or already active.")
    return curchan


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
        elif cmd == "active":
            cmd_active(curchan, args)
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
def send_join_message(producer, nick, channel):
    message = f"{nick} has joined"
    producer.send(channel, value=message.encode('utf-8'))


def send_leave_message(producer, nick, channel):
    message = f"{nick} has left"
    producer.send(channel, value=message.encode('utf-8'))


def send_leave_messages_on_all_channels(producer, nick, channels):
    for channel in channels:
        send_leave_message(producer, nick, channel)

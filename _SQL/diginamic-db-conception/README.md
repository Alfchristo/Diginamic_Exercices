# diginamic-db-conception

## TP réalisé avec Christ Mougani

## Conception d’une base de données de jeu vidéo

### Consignes
Vous êtes mandaté pour créer une base de données pour les serveurs d’un jeu
vidéo tel que Fall Guys, Among Us ou Golf With Your Friends. Si l’inspiration
vous manque, faites au plus simple.
Un jeu nécessite l’enregistrement de joueurs, d’un certain nombre de parties,
éventuellement différentes cartes sur lesquelles les parties se déroulent, un score
par partie, et un score global permettant d’établir un classement entre joueurs.
Les joueurs peuvent éventuellement disposer de skins ou d’items particuliers, et
potentiellement être en équipe avec d’autres joueurs.

### Dictionnaire des données

| Nom                   | Désignation                                   | Type  | Taille    | Entité
| --------------------- | --------------------------------------------- | ----- | --------- | ---------------	
| date_compte_joueur	| Date de création du compte du joueur	        | DATE	| 	        | Joueurs		
| date_creation	        | Date de création de l'équipe	                | DATE	| 	        | Equipes		
| date_partie	        | Date de la partie	                            | DATE	| 	        | Partie		
| description	        | Description de l'accessoire	                |VARCHAR| 255	    | Accessoires		
| durée_partie	        | Durée de la partie	                        | TIME	| 	        | Partie		
| email_joueur	        | Courriel du joueur	                        |VARCHAR| 25	    | Joueurs		
| id_acces	            | Identifiant de l'accessoire	                | Int	| 10	    | Accessoires		
| id_carte	            | Identifiant de la carte	                    | Int	| 10	    | Cartes		
| id_equipe	            | Identifiant de l'équipe	                    | Int	| 10	    | Equipes		
| id_joueur	            | Identifiant du joueur	                        | Int	| 10	    | Joueurs		
| id_partie	            | Identifiant de la partie	                    | Int	| 10	    | Partie		
| limite_joueur	        | Limite nombre de joueurs dans la carte	    | Int	| 3	        | Cartes		
| mdp_joueur	        | Mot de passe de compte du joueur	            |VARCHAR|20	        | Joueurs		
| nom_acces	            | Nom de l'accessoire	                        |VARCHAR| 65	    | Accessoires		
| nom_carte	            | Nom de la carte	                            |VARCHAR| 25	    | Cartes		
| nom_equipe	        | Nom de l'équipe	                            |VARCHAR| 25	    | Equipes		
| nom_joueur	        | Nom du joueur	                                |VARCHAR| 20	    | Joueurs		
| prenom_joueur	        | Prenom du joueur	                            |VARCHAR| 65	    | Joueurs		
| rang	                | Numero de rang	                            | Int	| 5	        | Rangs		
| role_equipe	        | Rôle des membres de l'équipe	                |VARCHAR| 65	    | Equipes		
| score_equipe	        | Score de l'équipe	                            | Int	| 15	    | Equipes		
| score_globale	        | Score globable des joueurs	                | Int	| 15	    | Rangs		
| score_partie	        | Score de la partie	                        | Int	| 10	    | Partie		
| taille_carte	        | Taille de la carte	                        | Int	| 25	    | Cartes		
| type_acces	        | Type d'accessoire	                            |VARCHAR| 65	    | Accessoires		
| type_carte	        | Type de la carte	                            |VARCHAR| 120	    | Cartes		


### MCD

![](/MCD.png)

### MLD

```
Cartes = (id_carte INT, taille_carte INT, nom_carte VARCHAR(50), limite_joueur SMALLINT, type_carte VARCHAR(20));
Parties = (id_partie INT, date_partie DATETIME, score_partie INT, duree_partie TIME, #id_carte);
Equipes = (id_equipe INT, nom_equipe VARCHAR(50), date_creation DATE, role_equipe VARCHAR(50), score_equipe INT);
Accessoires = (id_acces INT, type_acces VARCHAR(20), nom_acces VARCHAR(20), description VARCHAR(255));
Joueurs = (id_joueur INT, nom_joueur VARCHAR(20), prenom_joueur VARCHAR(20), date_compte_joueur DATE, email_joueur VARCHAR(20), mdp_joueur VARCHAR(20), #id_acces*, #id_equipe*);
a_un_Rang = (#id_joueur, #id_partie, rang INT, scores_globale INT);


```

### MPD

![](/MPD.png)

### SQL

```SQL
CREATE TABLE Accessoires (
  Id_acces    int(10) NOT NULL AUTO_INCREMENT, 
  type_acces  varchar(65) NOT NULL, 
  nom_acces   varchar(65) NOT NULL, 
  description varchar(255), 
  PRIMARY KEY (Id_acces));
CREATE TABLE Cartes (
  id_carte      int(10) NOT NULL AUTO_INCREMENT, 
  taille_carte  varchar(25) NOT NULL, 
  nom_carte     varchar(25) NOT NULL, 
  limite_joueur int(3) NOT NULL, 
  type_carte    varchar(120) NOT NULL, 
  PRIMARY KEY (id_carte));
CREATE TABLE Equipes (
  id_equipe     int(10) NOT NULL AUTO_INCREMENT, 
  nom_equipe    varchar(25) NOT NULL, 
  date_creation date NOT NULL, 
  role_equipe   varchar(65), 
  score_equipe  int(15), 
  PRIMARY KEY (id_equipe));
CREATE TABLE Joueurs (
  id_joueur            int(10) NOT NULL AUTO_INCREMENT, 
  nom_joueur           varchar(20) NOT NULL, 
  prenom_joueur        varchar(65) NOT NULL, 
  date_compte_joueur   date NOT NULL, 
  email_joueur         varchar(25) NOT NULL, 
  mdp_joueur           varchar(20) NOT NULL, 
  AccessoiresId_acces2 int(10) NOT NULL, 
  Equipesid_equipe     int(10) NOT NULL, 
  PRIMARY KEY (id_joueur));
CREATE TABLE Parties (
  id_partie      int(10) NOT NULL AUTO_INCREMENT, 
  date_partie    date NOT NULL, 
  score_partie   int(10), 
  duree_partie   time NOT NULL, 
  Cartesid_carte int(10) NOT NULL, 
  PRIMARY KEY (id_partie));
CREATE TABLE Rang (
  Joueursid_joueur int(10) NOT NULL, 
  Partiesid_partie int(10) NOT NULL, 
  rang             int(5) NOT NULL, 
  score_globale    int(15), 
  PRIMARY KEY (Joueursid_joueur, 
  Partiesid_partie));
ALTER TABLE Joueurs ADD CONSTRAINT FKJoueurs411306 FOREIGN KEY (AccessoiresId_acces2) REFERENCES Accessoires (Id_acces);
ALTER TABLE Parties ADD CONSTRAINT FKParties778403 FOREIGN KEY (Cartesid_carte) REFERENCES Cartes (id_carte);
ALTER TABLE Rang ADD CONSTRAINT FKRang117409 FOREIGN KEY (Joueursid_joueur) REFERENCES Joueurs (id_joueur);
ALTER TABLE Rang ADD CONSTRAINT FKRang623113 FOREIGN KEY (Partiesid_partie) REFERENCES Parties (id_partie);
ALTER TABLE Joueurs ADD CONSTRAINT FKJoueurs303588 FOREIGN KEY (Equipesid_equipe) REFERENCES Equipes (id_equipe);

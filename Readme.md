# Système de Planification d'emploi du temps Universitaire avec Google OR-Tools

## Description du Projet

Ce projet implémente un système de planification universitaire en utilisant **Google OR-Tools** pour optimiser
l'affectation des cours en fonction de contraintes telles que la disponibilité des professeurs, la disponibilité des
salles et les exigences spécifiques aux matières.

## Fonctionnalités

- **Planification Automatique** : Assigne les cours aux salles et aux professeurs en tenant compte des créneaux
  horaires.
- **Disponibilité des Professeurs** : Garantit que les professeurs sont planifiés uniquement lorsqu'ils sont
  disponibles.
- **Disponibilité des Salles** : Empêche la planification dans des salles non disponibles.
- **Contraintes des Cours** : Assure que chaque cours est enseigné par le professeur qui lui est assigné et respecte les
  limites minimales et maximales d'heures possibles.
- **Optimisation des Créneaux Horaires** : Maximise l'utilisation des créneaux disponibles.

## Installation

### Prérequis

- Python 3.10
- Gestionnaire de paquets pip
- La bibliothèque virtualenv

### Cloner le Dépôt

```bash
git clone https://github.com/WesleyEliel/university-course-timetable-planning.git
cd university-course-timetable-planning
```

### Installation des dépendances

Créez un environment virtuel avec virtualenv et activez-le

```bash
virtualenv venv
source ./venv/bin/activate 
```

Installez les dépendances

```bash
pip install requirements.txt  
```

## Utilisation

### Étape 1 : Modifier les Données à votre convenance dans le fichier main.py

Modifier le fichier ```main.py``` avec les professeurs, les salles, les cours et les disponibilités.

### Étape 2 : Exécuter le Planificateur

Lancez le script principal :

```bash
python main.py
```

### Étape 3 : Voir les Résultats

Si un emploi du temps valide est trouvé, il sera affiché dans la console.

## Structure du Projet

```
/
│── main.py                 # Point d'entrée pour résoudre la planification
│── scheduler/              # Definition de la classe principale pour la gestion des emplois du temps
│── models/                 # Définit les modèles orientés objet (Professeur, Salle, Cours, CréneauHoraire)
│── README.md                 # Documentation
```

## Exemple de Résultat

```
Emploi du temps optimal trouvé :

R.O et I.A planifié pour Prof_A dans la salle Salle_A sur le créneaux Lundi de 8h à 12h
R.O et I.A planifié pour Prof_A dans la salle Salle_A sur le créneaux Lundi de 14h à 18h
R.O et I.A planifié pour Prof_A dans la salle Salle_A sur le créneaux Mardi de 8h à 12h
Maths pour l' informatique planifié pour Prof_A dans la salle Salle_A sur le créneaux Mercredi de 8h à 12h
Administration Réseaux planifié pour Prof_B dans la salle Salle_B sur le créneaux Vendredi de 8h à 12h
Administration Réseaux planifié pour Prof_B dans la salle Salle_B sur le créneaux Vendredi de 14h à 18h
Sécurité Web & Mobile planifié pour Prof_C dans la salle Salle_C sur le créneaux Jeudi de 8h à 12h
Sécurité Web & Mobile planifié pour Prof_C dans la salle Salle_C sur le créneaux Jeudi de 14h à 18h

```

## Améliorations Futures

- Interface graphique pour une saisie plus facile des données
- API pour des intégrations externes
- Personnalisation dynamique des contraintes
- Ajout de nouvelles contraintes (Si possible, on veut que les heures d’une même matière soient réparties sur plusieurs
  jours au lieu d’être concentrées sur une seule journée. )

## Licence

Ce projet est sous licence....


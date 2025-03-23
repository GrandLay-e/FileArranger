# Réorganisation Automatique de Fichiers

Ce programme permet de réorganiser automatiquement les fichiers d'un dossier en les classant par type, année et mois de création.

## 📋 Fonctionnalités
- Classement automatique des fichiers par catégories (Documents, Images, Musique, Vidéos, Archives, Applications, etc.).
- Création de dossiers pour chaque type de fichier, année, et mois de création.
- Déplacement des fichiers vers leurs dossiers respectifs.
- Enregistrement des actions réalisées dans un fichier `Moving-process.log`.

## 📂 Types de fichiers pris en charge
Les types de fichiers sont définis dans le fichier `DICT.py` :
- **Documents** : `.pdf`, `.ods`, `.odt`, `.txt`, `.docx`, `.pptx`, `.xls`, `.csv`, `.epub`, `.rtf`, `.odg`, `.ris`, `.xlsx`, `.html`, `.css`, `.py`, `.php`, `.sql`, `.js`
- **Images** : `.jpg`, `.png`, `.bmp`, `.jpeg`, `.webp`
- **Musique** : `.mp3`, `.aac`, `.m4a`, `.wav`, `.opus`
- **Vidéos** : `.mp4`, `.avi`, `.mkv`, `.gif`
- **Archives** : `.zip`, `.rar`, `.gz`, `.deb`, `.iso`, `.7z`
- **Applications** : `.exe`, `.deb`, `.msi`, `.apk`, `.vmdk`, `.ova`, `.vbox`, `.vdi`

## 📌 Installation
1. Clonez ce dépôt ou téléchargez-le.
2. Assurez-vous d'avoir Python installé (version >= 3.6).
3. Installez les modules nécessaires (si besoin) :
```bash
Les bibliothèques utilisées (`logging`, `os`, `pathlib`, `time`) sont intégrées par défaut avec Python. Vous n'avez donc pas besoin d'installer de dépendances supplémentaires.
```

## 🚀 Utilisation
1. Placez tous les fichiers que vous souhaitez réorganiser dans un dossier spécifique.
2. Exécutez le script principal :
```bash
python main.py
```
3. Entrez le chemin complet du dossier lorsque demandé.
4. Le programme déplacera automatiquement les fichiers dans des sous-dossiers selon leur type, année et mois de création.

## 📖 Exemple de Structure Générée
```
Dossier Principal/
│
├── Documents/
│   ├── 2025/
│   │   └── Mars/
│   │       └── fichier.pdf
│
├── Images/
│   ├── 2024/
│   │   └── Décembre/
│   │       └── image.jpg
│
├── Moving-process.log
```

## 📄 Fichier de Log
Le fichier `Moving-process.log` contient l'historique de toutes les opérations de déplacement réalisées, incluant les chemins sources et destinations.

## 💡 Remarques
- Si un fichier portant le même nom existe déjà dans le dossier de destination, il sera remplacé automatiquement.
- En cas d'erreur de permission, le fichier sera ignoré et indiqué dans le fichier de log.

## 🔧 Améliorations Possibles
- Ajouter une interface graphique.
- Ajouter des options de personnalisation (choix des extensions, etc.).
- Ajouter une option de tri par date de modification ou d'accès au lieu de la date de création.


Créé par : SOW ABDALLAH


def extract_emails(input_file, output_file):
    try:
        # Ouvre le fichier d'entrée en mode lecture
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Lit toutes les lignes du fichier
            lines = infile.readlines()
        
        # Extrait les e-mails (partie avant ':')
        emails = [line.split(':')[0].strip() for line in lines if ':' in line]
        
        # Ouvre le fichier de sortie en mode écriture
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Écrit chaque e-mail sur une nouvelle ligne
            for email in emails:
                outfile.write(email + '\n')
                
        print(f"Extraction terminée. {len(emails)} e-mails enregistrés dans {output_file}")
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

# Exemple d'utilisation
if __name__ == "__main__":
    input_file = "input.txt"  # Remplacez par le nom de votre fichier d'entrée
    output_file = "emails.txt"  # Nom du fichier de sortie
    extract_emails(input_file, output_file)
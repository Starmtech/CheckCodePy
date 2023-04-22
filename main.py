import os
import ast
import subprocess


vulnerabilities = {
    'exec': 'Utilisation de la fonction exec',
    'eval': 'Utilisation de la fonction eval',
    'pickle': 'Utilisation de la bibliothèque pickle',
    'subprocess': 'Utilisation de la bibliothèque subprocess',
    'shell': 'Utilisation de la commande shell'
}


def static_analysis(filename):
    # Vérifie les erreurs de syntaxe avec ast
    try:
        with open(filename) as f:
            tree = ast.parse(f.read())
    except SyntaxError as e:
        print(f"Erreur de syntaxe dans le fichier {filename}: {e}")
        
        
    pylint_result = subprocess.run(["pylint", filename], stdout=subprocess.PIPE)
    pylint_output = pylint_result.stdout.decode('utf-8')
    if 'Your code has been rated' in pylint_output:
        print(f"Le fichier {filename} a été noté comme suit par pylint:")
        print(pylint_output)


def dynamic_analysis():
    # Exécute les tests automatisés avec pytest
    pytest_result = subprocess.run(["pytest"], stdout=subprocess.PIPE)
    pytest_output = pytest_result.stdout.decode('utf-8')
    if 'failed' in pytest_output:
        print("Des tests ont échoué. Voici la sortie de pytest :")
        print(pytest_output)


def dependency_check():
    pipdeptree_result = subprocess.run(["pipdeptree"], stdout=subprocess.PIPE)
    pipdeptree_output = pipdeptree_result.stdout.decode('utf-8')
    if 'WARNING' in pipdeptree_output:
        print("Attention : des dépendances obsolètes ou vulnérables ont été trouvées :")
        print(pipdeptree_output)


def configuration_check():
    for filename in ['settings.py', 'config.py', 'secrets.py']:
        if os.path.isfile(filename):
            with open(filename) as f:
                for line in f.readlines():
                    if 'api_key' in line or 'password' in line:
                        print(f"Attention : la chaîne de caractères suivante a été trouvée dans {filename} : {line.strip()}")


def security_check():
    # Vérifie la conformité aux normes de sécurité avec CIS Benchmarks
    cis_benchmarks_result = subprocess.run(["cis-cat", "-r", "-n", "python27"], stdout=subprocess.PIPE)
    cis_benchmarks_output = cis_benchmarks_result.stdout.decode('utf-8')
    if 'BENCHMARK RESULTS SUMMARY' in cis_benchmarks_output:
        print("Le code respecte les CIS Benchmarks.")
    else:
        print("Attention : le code ne respecte pas les CIS Benchmarks. Voici la sortie de cis-cat :")
        print(cis_benchmarks_output)


def full_analysis():
    while not os.path.isfile(filename):
        filename = input("Entrez le nom du fichier python à analyser : ")

print(f"Analyse du fichier {filename} en cours...")
static_analysis(filename)
dynamic_analysis()
dependency_check()
configuration_check()
security_check()
print("Analyse terminée.")
if name == 'main':
full_analysis()

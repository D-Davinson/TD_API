from pydantic import BaseModel, validator

class Patient(BaseModel):
    nom: str
    prenom: str
    ssn: str
    
    @validator('ssn')
    def validate_ssn(cls, ssn):
        if len(ssn) != 15:
            raise ValueError('Le numéro de sécurité sociale doit contenir exactement 13 chiffres.')
        if ssn[0] not in ['1', '2']:
            raise ValueError('Le premier chiffre du numéro de sécurité sociale doit être 1 pour un homme ou 2 pour une femme.')
        annee = int(ssn[1:3])
        if annee < 0 or annee > 99:
            raise ValueError('L\'année de naissance dans le numéro de sécurité sociale est invalide.')
        mois = int(ssn[3:5])
        if mois < 1 or mois > 12:
            raise ValueError('Le mois de naissance dans le numéro de sécurité sociale est invalide.')
        department = int(ssn[5:7])
        if department < 1 or department > 99:
            raise ValueError('Le département de naissance dans le numéro de sécurité sociale est invalide.')
        pays_id = int(ssn[7:10])
        if pays_id < 1 or pays_id > 999:
            raise ValueError('L\'identifiant du pays de naissance dans le numéro de sécurité sociale est invalide.')
        anniversaire_index = int(ssn[10:13])
        if anniversaire_index < 1 or anniversaire_index > 999:
            raise ValueError('L\'indice de naissance dans le numéro de sécurité sociale est invalide.')
        control_key = int(ssn[14:15])
        if control_key < 0 or control_key > 99:
            raise ValueError('La clé de control dans le numéro de sécurité sociale est invalide.')
        if int(ssn) % 97 != 0:
            raise ValueError('La clef de contrôle dans le numéro de sécurité sociale est invalide.')
        
        return ssn

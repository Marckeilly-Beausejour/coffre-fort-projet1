# coffre-fort-projet1

# Livrable 1

## Descrition et fonction

#### Un système de coffre-fort intelligent RFID. Le coffre-fort s’ouvrira avec une carte RFID précise. Si le coffre est verrouillé,   une LED rouge s’affichera, si le coffre est ouvert, une LED verte s’affichera et si le coffre est bloqué en raison de trop de tentatives échouées, une LED jaune va s’afficher et un timer va apparaître sur l’écran permettant de savoir dans combien de temps on peut réessayer. Il y aura aussi un temps maximal pendant lequel le coffre peut être ouvert et après cela, une alarme va sonner pour avertir que le coffre est ouvert (un son différent de celui pour le badge refusé/accepté). Le Reed switch va permettre de savoir si la porte est ouverte ou fermée et ensuite de partir le potentiomètre. Le servo, quant à lui, est le mécanisme permettant d’ouvrir le coffre-fort. Le Traffic Light va permettre de voir l’état du coffre, vert c’est ouvert, jaune c’est en attente du compte à rebours et rouge c’est barré. Il y aura aussi un écran permettant d’afficher le compte à rebours d’ouverture, le compte à rebours du blocage et le statut après avoir scanné une carte (verrouillé/déverrouillé). Le buzzer produira une mélodie différente pour chaque état, « Bip » pour un déverrouillage, « Bip Bip » pour un échec et « Bip Bip Bip … » pour l’alarme de la porte ouverte trop longtemps.

## Liste composants 

#### Arduino
#### Capteur RFID RC522
#### Servo 
#### Reed switch
#### Potentiomètre
#### Écran LCD
#### Buzzer
#### Traffic light 
#### Breadboard
#### Source d'alimentation


## Attribution des broches 

| Composant | Broche Arduino |
|---|---|
| RFID RC522 (SDA/SS) | D10 |
| RFID RC522 (SCK) | D13 |
| RFID RC522 (MOSI) | D11 |
| RFID RC522 (RST) | D12 |
| Servo moteur | D5 |
| Buzzer | D6 |
| Reed switch | D7 |
| LED verte | D3 |
| LED jaune | D4 |
| LED rouge | D5 |
| LCD (SDA) | A4 |
| LCD (SCL) | A5 |
| Potentiomètre | A0 |


## Répartion des taches 

## Mathieu 
#### Il fera l’installation du RFID, le servo, le Reed switch, le buzzer et l’écran. Côté script principalement.

## Samuel 

#### Il fera la maquette ainsi que l’installation des câbles, l’aspect esthétique et fonctionnel du coffre, la programmation du potentiomètre et du Traffic Light.

# Livrable 2



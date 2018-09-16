# Skill Alexa Bus Toulouse

## Description

Non-official Alexa skill to get info about Tisséo Toulouse buses (France).

## Usage

> - Alexa, demande à bus toulouse quand passe le prochain bus à l'arrêt Moulin Armand
> - Le bus 62 à destination de Ramonville passera dans 5 minutes.

## Useful

- [Alexa development console](https://developer.amazon.com/alexa/console/ask)
- [AWS Lambda console](https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1)

### Lambda 

- Alexa skill kit is not available in Paris AWS datacenter (available in Ireland)
- Make sure you put `bus_toulouse.handler` in Gestionnaire

## License

L'utilisation de l'API Tisséo est soumise à la licence ODbL <http://data.grandtoulouse.fr/la-licence>

## TODO

- [ ] Ajout de la possibilité de demander les passages à un arrêt pour une ligne ou destination particulière (ex : quand passe le prochain bus à destination de Ramonville à l'arrêt Moulin Armand ? **OU** quand passe le prochain bus L6 à l'arrêt Moulin Armand ?)
- [ ] Lorsque le nom de l'arrêt existe dans plusieurs villes (ex : Roses). Demander à l'utilisateur de confirmer sa ville
- [ ] Gestion d'arrêts favoris, ou d'itinéraires favoris (si un seul arrêt favori, permettre de demander : Quand passe le prochain bus? **OU** Quand passe le 81? **OU** Quand passe le 109 pour Labège?)
- [ ] Déterminer les arrêts à proximité à partir de l'adresse définie dans Alexa (en demandant confirmation qu'elle est correcte)
- [ ] Gestion des lignes de métro et tramway (en particulier pour ne pas dire "le bus B")
- [ ] Permettre le calcul d'itinéraire en indiquant une adresse ou un point d'intérêt (ex : calcule l'itinéraire pour aller au Gaumont Labège)
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

- [ ] Lorsque le nom de l'arrêt est le même pour plusieurs villes. Demander à l'utilisateur de confirmer sa ville
- [ ] Gestion d'arrêts favoris? Ou d'itinéraires favoris?
- [ ] Gestion des lignes de métro et tramway (en particulier pour ne pas dire "le bus B")
# Skill Alexa Bus Toulouse

## Description

![Bus Toulouse Alexa skill icon](/icons/icon_108_A2Z.png)

Non-official Alexa skill to get info about Tisséo Toulouse buses (France).

# Release note

## v0.1.0 - 17/09/2018

### Usage

You can ask for the schedules at a specified **stop area**.

> - Alexa, demande à bus toulouse quand passe les prochains bus à l'arrêt **Moulin Armand**
> - A l'arrêt moulin armand, Le bus 81, à destination de Université Paul Sabatier, passera dans 3 minutes. Le bus L6, à destination de Castanet-Tolosan, passera dans 4 minutes. Le bus L6, à destination de Ramonville, passera dans 7 minutes. Le bus 81, à destination de Castanet-Tolosan, passera dans 17 minutes.

You can ask even filter with the **bus line**.

> - Alexa, demande à bus toulouse quand passe les prochains bus **L6** à l'arrêt Moulin Armand
> - A l'arrêt moulin armand, Le bus L6, à destination de Castanet-Tolosan, passera dans 2 minutes. Le bus L6, à destination de Ramonville, passera dans 4 minutes.

And also filter with the **destination**.

> - Alexa, demande à bus toulouse quand passe les prochains bus à destination de **Castanet-Tolosan** à l'arrêt Moulin Armand
> - A l'arrêt moulin armand, Le bus L6, à destination de Castanet-Tolosan, passera dans 3 minutes. Le bus 81, à destination de Castanet-Tolosan, passera dans 10 minutes.

-------------------------------

## Requirements

You need [to obtain an API key for Tisséo](https://data.toulouse-metropole.fr/explore/dataset/api-temps-reel-tisseo/), and set the environment variable `TISSEO_API_KEY` with it.

## Useful

- [Alexa development console](https://developer.amazon.com/alexa/console/ask)
- [AWS Lambda console](https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1)
- [Icon generation](https://developer.amazon.com/fr/docs/tools/icon-builder.html)

### Lambda 

- Alexa skill kit is not available in Paris AWS datacenter (available in Ireland)
- Make sure you put `bus_toulouse.handler` in Gestionnaire

## License

L'utilisation de l'API Tisséo est soumise à la licence ODbL <http://data.grandtoulouse.fr/la-licence>

## TODO

- [ ] Lorsque le nom de l'arrêt existe dans plusieurs villes (ex : Roses). Demander à l'utilisateur de confirmer sa ville
- [ ] Gestion d'arrêt favori : Quand passe le prochain bus? **OU** Quand passe le 81? **OU** Quand passe le 109 pour Labège?
- [ ] Gestion d'itinéraires favoris : Prochain bus pour aller au travail?
- [ ] Déterminer les arrêts à proximité à partir de l'adresse définie dans Alexa (en demandant confirmation qu'elle est correcte)
- [ ] Permettre le calcul d'itinéraire en indiquant une adresse ou un point d'intérêt (ex : calcule l'itinéraire pour aller au Gaumont Labège)
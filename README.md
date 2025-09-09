2026.compas-conference.fr

# Installation

La commande `bundle` est fournie par le paquet `ruby-bundler` sur Debian.

```sh
bundle config set --local path 'vendor/bundle'
bundle install
```

# Générer et prévisualiser le site en local

```sh
bundle exec jekyll s
```
Le site est ensuite accessible à l'adresse http://127.0.0.0:4000. Lors d'une
modification à un fichier source, le site est automatiquement regénéré et il
suffit d'actualiser la page dans son navigateur.

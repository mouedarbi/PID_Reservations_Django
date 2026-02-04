# Logbook - Journal de développement

## 27 janvier 2026 - 15:30 - Jour 1

### Progrès réalisés :
- Création d'un système d'administration personnalisé avec interface moderne inspirée du template fourni
- Intégration du template open source "Tickety" pour le dashboard admin
- Création de la table de liaison manquante `RepresentationReservation`
- Développement d'un dashboard avec graphiques et indicateurs de performance
- Mise en place de deux interfaces admin coexistantes : standard et personnalisée

### Erreurs rencontrées et solutions :

1. **Erreur : SystemCheckError - Admin.E013**
   - Description : `The value of 'filter_horizontal[0]' cannot include the ManyToManyField 'artist_types', because that field manually specifies a relationship model.`
   - Solution : Suppression de `filter_horizontal = ('artist_types',)` dans le fichier `catalogue/admin.py` car le champ `artist_types` utilise un modèle de relation intermédiaire (`ArtistTypeShow`)

2. **Erreur : AttributeError - module 'catalogue.models.artist' has no attribute 'index'**
   - Description : Problème d'import dans le fichier `catalogue/urls.py` causé par un conflit entre `from . import *` dans le fichier `__init__.py`
   - Solution : Remplacement de `from . import *` par des imports explicites dans `catalogue/views/__init__.py`

3. **Erreur : KeyError at /admin-dashboard/ - 'log_entries'**
   - Description : La vue `AdminDashboardView` tentait d'accéder à des variables de contexte admin spécifiques
   - Solution : Modification de la vue pour inclure les variables de contexte nécessaires et création d'un template spécifique `admin_dashboard.html`

4. **Erreur : ModuleNotFoundError - No module named 'catalogue.urls.admin_dashboard_urls'**
   - Description : Problème d'import dans le fichier `reservations/urls.py`
   - Solution : Approche simplifiée en ajoutant directement la route dans le fichier principal

### Fichiers créés/importants modifiés :
- `catalogue/models/representation_reservation.py` - Nouvelle table de liaison
- `catalogue/templates/admin/admin.html` - Template de base admin personnalisé
- `catalogue/templates/admin/admin_dashboard.html` - Template spécifique pour le dashboard
- `catalogue/views/admin_views.py` - Vue pour le dashboard personnalisé
- `catalogue/static/admin/css/original-styles.css` - Fichiers CSS du template
- `catalogue/static/admin/js/original-index.js` - Fichiers JS du template

### Nombreuses insertions (~20k lignes) :
- Expliquées par l'intégration du template open source "Tickety" comprenant les fichiers CSS et JS nécessaires à l'interface admin moderne.

### Objectifs atteints :
- ✓ Interface admin standard fonctionnelle via `/admin/`
- ✓ Dashboard personnalisé accessible via `/admin-dashboard/`
- ✓ Deux interfaces coexistant harmonieusement
- ✓ Design moderne inspiré du template fourni
- ✓ Fonctionnalités de visualisation des données
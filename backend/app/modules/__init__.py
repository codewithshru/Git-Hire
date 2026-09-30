"""Feature modules of the GitHire modular monolith.

Each module follows the same internal shape:
router.py · schemas.py · models.py · repository.py · service.py

Cross-module calls go through service.py functions ONLY — never another
module's models or repository. This is what keeps services extractable later.
"""

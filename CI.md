# Asset CI

Every PR and default-branch push validates all tracked PNG logos: image type,
positive dimensions, PNG chunk integrity and actual pixel decoding. NUL-delimited
Git filenames correctly handle accents, spaces and quotes. The baseline contains
10,777 valid PNGs; no asset exceptions, renames or image rewrites are needed.

Run `uv run --no-project --with-requirements .github/requirements.txt python .github/scripts/check-assets.py`
locally with Python and uv 0.12.10. Pillow is explicitly versioned and maintained
by Renovate. Run `php -l utilities/generate-all-logos-mosaics.php` for PHP syntax.
The CI PHP interpreter follows the Ubuntu 24.04 runner image; the helper also
passes PHP 8.4 syntax validation. Its mosaic-generation side effects are not run
against the repository as a validation step.

The shared `ci / required` gate rejects missing, failed, cancelled or skipped
prerequisites; dispatch guards check explicitly requested PR SHAs before and
after validation. Tokens are read-only, action references use full version tags,
and validation rejects tracked-file changes. Upstream artwork and attribution
are preserved. A web framework, formatter or dummy application test would not
provide useful coverage for this asset collection.

Checks prove image readability, not visual design, broadcaster identity or
mosaic-rendering behavior. Those remain review tasks. Protect the default branch
with strict up-to-date `ci / required` from GitHub Actions, enforced administrators,
zero required reviews and no force-push/deletion bypass. Renovate uses the shared
base preset; automerge stays off until the policy and settings are verified.

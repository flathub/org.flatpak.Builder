#!/bin/bash

FLATPAK_BINARY=$(flatpak-spawn --host which flatpak 2>/dev/null)

export FLATPAK_BINARY
export FLATPAK_USER_DIR="$HOME/.local/share/flatpak"

CMD=flatpak-builder
ARGS=(
  --verbose
  --force-clean
  --sandbox
  --keep-build-dirs
  --override-source-date-epoch 1321009871
  --user
  --install-deps-from=flathub
  --ccache
  --mirror-screenshots-url=https://dl.flathub.org/media
  --repo=repo
  builddir
  "$@"
)

echo -n "Running:"
printf ' %q' "$CMD" "${ARGS[@]}"
echo

exec "$CMD" "${ARGS[@]}"

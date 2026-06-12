#!/usr/bin/env bash
# Telecharge le JAR TweetyProject (module arg.dung) requis par la couche
# symbolique. Necessite un JDK (Java 11+) sur la machine.
set -euo pipefail

VERSION="${TWEETY_VERSION:-1.30}"
JAR="org.tweetyproject.arg.dung-${VERSION}-with-dependencies.jar"
URL="https://tweetyproject.org/builds/${VERSION}/${JAR}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${ROOT}/lib/tweety-arg-dung-${VERSION}.jar"

mkdir -p "${ROOT}/lib"
if [ -f "${DEST}" ]; then
  echo "[setup_tweety] deja present: ${DEST}"
  exit 0
fi

echo "[setup_tweety] telechargement ${URL}"
curl -fL --retry 3 -o "${DEST}" "${URL}"
echo "[setup_tweety] OK -> ${DEST}"

if command -v java >/dev/null 2>&1; then
  java -version
else
  echo "[setup_tweety] ATTENTION: 'java' introuvable. Installer un JDK 11+." >&2
fi

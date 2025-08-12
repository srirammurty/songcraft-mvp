#!/usr/bin/env bash
DIR="indian-music-starter"
OUT="${DIR}.zip"
if [ ! -d "$DIR" ]; then
  echo "$DIR missing"
  exit 1
fi
rm -f "$OUT"
zip -r "$OUT" "$DIR"
echo "Created $OUT"

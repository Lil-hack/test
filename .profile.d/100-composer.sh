export PATH=$HOME/.heroku/php/bin:$PATH:$HOME/vendor/bin
mlib="/sys/fs/cgroup/memory/memory.limit_in_bytes"
if [[ -f "$mlib" ]]; then
export COMPOSER_MEMORY_LIMIT=${COMPOSER_MEMORY_LIMIT:-$(cat "$mlib")}
fi
export COMPOSER_MIRROR_PATH_REPOS=${COMPOSER_MIRROR_PATH_REPOS:-1}
export COMPOSER_NO_INTERACTION=${COMPOSER_NO_INTERACTION:-1}
export COMPOSER_PROCESS_TIMEOUT=${COMPOSER_PROCESS_TIMEOUT:-0}

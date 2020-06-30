export PATH="$HOME/.heroku/php/bin:$HOME/.heroku/php/sbin:$PATH"

# read memory limit of dyno
mlib="/sys/fs/cgroup/memory/memory.limit_in_bytes"
# get php.ini location; don't forget to suppress INI scan dir to prevent e.g. New Relic from starting
php_ini_path=$(PHP_INI_SCAN_DIR= php -r 'echo get_cfg_var("cfg_file_path");')
if [[ -f "$mlib" && -n "$php_ini_path" ]]; then
	php_cli_ini_path=$(dirname "$php_ini_path")/php-cli.ini
	# create php-cli.ini from php.ini unless it exists
	# we can't cp -n instead because php_ini_path would already be php-cli.ini and that would error
	if [[ "$php_ini_path" != "$php_cli_ini_path" ]]; then
		cp "$php_ini_path" "$php_cli_ini_path"
	fi
	# compute memory limit, up to 16 GB
	max_memory_limit=$(( 16 * 1024 * 1024 * 1024 ))
	sys_memory_limit=$(cat "$mlib")
	memory_limit=$(( sys_memory_limit > max_memory_limit ? max_memory_limit : sys_memory_limit ))
	# append to php-cli.ini
	echo $'\n;inserted by ~/.profile.d/ script' >> "$php_cli_ini_path"
	echo "memory_limit=$memory_limit" >> "$php_cli_ini_path"
fi


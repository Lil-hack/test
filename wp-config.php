<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */


define("DB_NAME", "site2");
define("DB_USER", "admin");
define("DB_PASSWORD", "12345678");
define("DB_HOST", "mydb-inst.clqpzxakexws.eu-central-1.rds.amazonaws.com");

  /** MySQL database port  */
  // define("DB_PORT", "3306");

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('SECURE_AUTH_KEY',  'e[I:g<CpHB-|=6$u!x+jiefiu0jVLd8#N6@*@ldv9|euYBh6?]I=01ROkuv c-Lq');
define('LOGGED_IN_KEY',    'tv{*-,-]{@cOA]gDf&_-vu2:,e*h|sdTP7gG-Zmr-wt4(1G2u8b9FniJA#{!7(w5');
define('NONCE_KEY',        'f2L,|8XlmqkH5>4gvygUw]&lD>+8A-$YKoa34]vWP%Mm1 oVXyM8;=z>n&K-L% 7');
define('AUTH_SALT',        '*w#xU#@<:Xa_B%1Vu&l#lJUO/{iu/T;HIbmd?~^^qOl$A_ob{o4a3-?o~5YDHIry');
define('SECURE_AUTH_SALT', '~4E]&VaU(Be)]ni}nf]F0Su+-c@x`u}P0(!!`CdJw7CX.O=)9MNEW+c5,*aWLH;a');
define('LOGGED_IN_SALT',   '8jkkUdZ!w38+C0QqO%|z+Be2gEQ{d1v<FwB+5=K[97;GcW/+%(.G+fn}Ct]/Q@nN');
define('NONCE_SALT',       'g$m.~Xz|[IDGV9vZ@IcBn#<omNC~%`<0,M*T||6y(-),W!t my|kVG+!s-0;`tYu');


/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

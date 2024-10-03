cosmic-ray init cray.toml cray.sqlite;  # creamos la bases de datos con todo lo que deberia correr
cosmic-ray --verbosity=INFO baseline cray.toml;  # baseline chequea que codigo inmitado funciona
cr-report cray.sqlite --show-pending; # ver trabajos pendientes
time cosmic-ray --verbosity=INFO exec cray.toml cray.sqlite;  # ejecutamos
cr-html cray.sqlite > report.html;  # creamos un reporte
cr-rate cray.sqlite; # survival rate

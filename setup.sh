mkdir -p ~/.pygame/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.pygame/config.toml

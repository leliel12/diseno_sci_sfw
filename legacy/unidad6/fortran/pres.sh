# nvim $(find . -type f | sort)

class="$1"

alacritty -e nvim $(find "$class" -type f \( -name "*.md" -or -name "*.f90" \) | sort) &
sxiv "$class/figs"

# start X at login
if status --is-login
    if test -z "$DISPLAY" -a $XDG_VTNR -eq 1
        exec startx -- -keeptty
    end
end

set -x fish_startup_command 'archey'

if set -q fish_startup_command
    eval $fish_startup_command
    set -e fish_startup_command
end

set -x LC_ALL en_US.UTF-8
set -x LC_CTYPE en_US.UTF-8


export MESA_DIR=/usr/share/mesa/
export MESA_CACHES_DIR=$HOME/.cache/mesa/

export PGPLOT_DIR=/usr/lib64/mesa/pgplot
export OMP_NUM_THREADS=$(nproc)

_star () {
    # Set
    IFS=$'\n' tmp=( $(compgen -W "$(ls "/usr/share/mesa/star-test-suite")" -- "${COMP_WORDS[$COMP_CWORD]}" ))
    COMPREPLY=( "${tmp[@]// /\ }" )
}
complete -o default -F _star mesa-star-test

_binary () {
    # Set
    IFS=$'\n' tmp=( $(compgen -W "$(ls "/usr/share/mesa/binary-test-suite")" -- "${COMP_WORDS[$COMP_CWORD]}" ))
    COMPREPLY=( "${tmp[@]// /\ }" )
}
complete -o default -F _binary mesa-binary-test
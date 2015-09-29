
export MESA_DIR=/usr/share/mesa/
export MESA_CACHES_DIR=$HOME/.cache/mesa/

export PGPLOT_DIR=/usr/lib64/mesa/pgplot
export OMP_NUM_THREADS=$(nproc)


alias mesa-star="LD_LIBRARY_PATH=/usr/lib64/mesa /usr/bin/mesa-star"
alias mesa-binary="LD_LIBRARY_PATH=/usr/lib64/mesa /usr/bin/mesa-binary"


_star () {
    # Set
    IFS=$'\n' tmp=( $(compgen -W "$(ls "/usr/share/mesa/star-test")" -- "${COMP_WORDS[$COMP_CWORD]}" ))
    COMPREPLY=( "${tmp[@]// /\ }" )
}
complete -o default -F _star mesa-star

_binary () {
    # Set
    IFS=$'\n' tmp=( $(compgen -W "$(ls "/usr/share/mesa/binary-test")" -- "${COMP_WORDS[$COMP_CWORD]}" ))
    COMPREPLY=( "${tmp[@]// /\ }" )
}
complete -o default -F _binary mesa-binary
{

    class MountError extends Error {}
    class ThreadError extends MountError {}

    let errors = {
        MountError
        , ThreadError
    }


    lib.expose({ errors })
}

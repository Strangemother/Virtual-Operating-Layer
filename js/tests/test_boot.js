describe('Boot', function(){

    describe('Threads', function(){
        it('should start call threat start', function(done){
            window.lib = unitjs.spy()

            var loadFunc = function(){

                Assets.load('initial', function(){
                    var mock = unitjs.mock(lib.threads)
                    // window.m = mock
                    mock.expects('start').calledWith(1)
                    done()
                })
            }
            var errFunc = function(err){
                test.fail(err)
            }

            unitjs.then(loadFunc)

        })

    })

})

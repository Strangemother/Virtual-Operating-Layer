/* This [single Thread] boots from a lib start Threads.
the _head_ imports the required assets from FILE[initializeThread]
Any additional work is handled by the the pook broker. */
importScripts('./head.js', '../assets.js')
Assets.load('initializeThread')
console.log('thread')

lib.log('Apples')

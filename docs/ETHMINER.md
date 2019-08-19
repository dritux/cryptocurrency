https://ethermine.org/miners/e83e059f243298151a14d867d56aa9806581265d/dashboard


Mining command line

./ethminer/ethminer -G -F http://eth-eu.dwarfpool.com:80/0xea7263feb7d8a8ab0a11eedd8f1ce04412ab0820

You can determine your rigs separately for better statistic. Determine workername with letters and numbers

ethminer.exe -G -F http://eth-eu.dwarfpool.com:80/YOUR_WALLET/YOUR_WORKER

You can also mine direct to any exchange

To enable email-monitoring of your worker, use email in url. To disable monitoring, restart your miner without email.

ethminer.exe -G -F http://eth-eu.dwarfpool.com/YOUR_WALLET/YOUR_WORKER/EMAIL

and without workers

ethminer.exe -G -F http://eth-eu.dwarfpool.com/YOUR_WALLET/EMAIL

Example wallet 0xea7263feb7d8a8ab0a11eedd8f1ce04412ab0820, worker rig1 and mail@example.com for monitoring



./ethminer/ethminer -G -F http://eu1.ethpool.org/0xe83e059f243298151a14d867d56aa9806581265d/dellcasa/dritec@gmail.com



./ethminer/ethminer -G -F http://eth-eu.dwarfpool.com:80/0xea7263feb7d8a8ab0a11eedd8f1ce04412ab0820



./ethminer/ethminer -C -F http://eth.pool.minergate.com:55751/dritec@gmail.com --disable-submit-hashrate


./ethminer/ethminer -epool us1.ethermine.org:4444 -ewal \
0xe83e059f243298151a14d867d56aa9806581265d ETH -epsw x -dpool \
stratum+tcp://dcr.suprnova.cc:3252 -dwal Dritux.my -dpsw x

ethminer -G -F us1.ethermine.org/0xe83e059f243298151a14d867d56aa9806581265d/dritec@gmail.com --cl-local-work 256 --cl-global-work 16384
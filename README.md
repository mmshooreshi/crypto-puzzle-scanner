# crypto-puzzle-scanner
This code generates random set of bitcoin public and private keys in range of one of the puzzles, in order to solve the puzzle.


BTC Puzzles Table:
| **# Bits** |      **Range (HEX)**      |       **Private Key**       |    **Wallets with LOTS OF BTCs**   |
| :--------: | :-----------------------: | :-------------------------: | :--------------------------------: |
|     ...    |            ...            |             ...             |                 ...                |
|     24     |  800000     -    ffffff   | 0000...00000000000000dc2a04 |  1rSnXMr63jdCuegJFuidJqWxUPV7AtUf7 |
|     25     |  1000000    -    1ffffff  | 0000...00000000000001fa5ee5 | 15JhYXn6Mx3oF4Y7PcTAv2wVVAuCFFQNiP |
|     26     |  2000000    -    3ffffff  | 0000...0000000000000340326e | 1JVnST957hGztonaWK6FougdtjxzHzRMMg |
|     27     |  4000000    -    7ffffff  | 0000...00000000000006ac3875 | 128z5d7nN7PkCuX5qoA4Ys6pmxUYnEy86k |
|     28     |  8000000    -    fffffff  | 0000...0000000000000d916ce8 | 12jbtzBb54r97TCwW3G1gCFoumpckRAPdY |
|     ...    |            ...            |             ...             |                 ...                |
|     62     | 2000..000   -   3fff..fff | 0000...0000363d541eb611abee | 1Me6EfpwZK5kQziBwBfvLiHjaPGxCKLoJi |
|     63     | 4000..000   -   7fff..fff | 0000...00007cce5efdaccf6808 | 1NpYjtLira16LfGbGwZJ5JbDPh3ai9bjf4 |
|     64     | 8000..000   -   ffff..fff |           Unsolved          | 16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN |
|     65     | 1000..000   -   1fff..fff | 0000...0001a838b13505b26867 | 18ZMbwUFLMHoZBbfpCjUJQTCMCbktshgpe |
|     66     | 2000..000   -   3fff..fff |           Unsolved          | 13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so |
|     67     | 4000..000   -   7fff..fff |           Unsolved          | 1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9 |
|     68     | 8000..000   -   ffff..fff |           Unsolved          | 1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ |
|     69     | 1000..000   -   1fff..fff |           Unsolved          | 19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG |
|     70     | 2000..000   -   3fff..fff | 0000...00349b84b6431a6c4ef1 | 19YZECXj3SxEZMoUeJ1yiPsw8xANe7M7QR |
|     71     | 4000..000   -   7fff..fff |           Unsolved          | 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU |
|     ...    |            ...            |             ...             |                 ...                |

You may find some of these puzzles here: https://privatekeys.pw/puzzles/bitcoin-puzzle-tx

main = do
    content <- readFile "input.txt"
    let input = map (read::String->Int) $ lines content
    print $ head [i * j * k | i <- input, j <- input, k <- input, i + j + k == 2020]
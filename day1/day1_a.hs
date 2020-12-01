main = do
    content <- readFile "input.txt"
    let input = map (read::String->Int) $ lines content
    print $ head [i * j | i <- input, j <- input, i + j == 2020]
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

public class Day3B {

  private static final char TREE = '#';

  public static void main(String[] args) throws IOException {
    var map = Files.lines(Paths.get("input.txt"), Charset.defaultCharset())
        .map(String::toCharArray)
        .toArray(char[][]::new);

    System.out.println(LongStream.of(
        countTrees(1, 1, map),
        countTrees(3, 1, map),
        countTrees(5, 1, map),
        countTrees(7, 1, map),
        countTrees(1, 2, map)
    ).reduce(1, (a, b) -> a * b));

  }

  private static int countTrees(int right, int down, char[][] map) {
    int trees = 0;

    for (int x = 0, y = 0; y < map.length; x += right, y += down) {
      trees += map[y][x % map[y].length] == TREE ? 1 : 0;
    }

    return trees;
  }
}

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Day3A {

  private static final char TREE = '#';

  public static void main(String[] args) throws IOException {
    var map = Files.lines(Paths.get("input.txt"))
        .map(String::toCharArray)
        .toArray(char[][]::new);

    int trees = 0;

    for (int x = 0, y = 0; y < map.length; x += 3, y++) {
      if (map[y][x % map[y].length] == TREE) trees++;
    }

    System.out.println(trees);
  }
}

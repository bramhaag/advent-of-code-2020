import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Day3A {

  private static final char TREE = '#';

  public static void main(String[] args) throws IOException {
    var map = Files.lines(Paths.get("input.txt"), Charset.defaultCharset())
        .map(String::toCharArray)
        .toArray(char[][]::new);

    int trees = 0;

    for (int x = 0, y = 0; y < map.length; x += 3, y++) {
      trees += map[y][x % map[y].length] == TREE ? 1 : 0;
    }

    System.out.println(trees);
  }
}

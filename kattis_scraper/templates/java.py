def java_template(name):
    return [
        "import java.util.*;",
        "import java.io.*;",
        "import java.math.*;",
        "",
        f"public class {name} {{",
        "",
        f"    public void {name}() throws IOException {{",
        "        ",
        "    }",
        "",
        "    static final boolean RUN_TIMING = false;",
        "    static final boolean AUTOFLUSH = false;",
        "    static final boolean FILE_INPUT = false;",
        "    static final boolean FILE_OUTPUT = false;",
        "",
        "    static int iinf = 0x3f3f3f3f;",
        "    static long inf = (long) 1e18 + 10;",
        "    static int mod = (int) 1e9 + 7;",
        "",
        "    static char[] inputBuffer = new char[1 << 20];",
        "    static PushbackReader in = new PushbackReader(new BufferedReader(new InputStreamReader(System.in)), 1 << 20);",
        "    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)), AUTOFLUSH);",
        "",
        "    // int data-type",
        "    public int ipar() throws IOException { return Integer.parseInt(spar()); }",
        "    public int[] iapar(int n) throws IOException {",
        "        int[] arr = new int[n];",
        "        for (int i = 0; i < n; i++) arr[i] = ipar();",
        "        return arr;",
        "    }",
        "    public void sort(int[] a) {",
        "        shuffle(a);",
        "        Arrays.sort(a);",
        "    }",
        "    public static void printArray(int[] arr) {",
        "        for (int i = 0; i<arr.length; i++) out.print(arr[i] + \" \");",
        "        out.println();",
        "    }",
        "",
        "    // long data-type",
        "    public long lpar() throws IOException { return Long.parseLong(spar()); }",
        "    public long[] lapar(int n) throws IOException {",
        "        long[] arr = new long[n];",
        "        for (int i = 0; i < n; i++) arr[i] = lpar();",
        "        return arr;",
        "    }",
        "    public static void printArray(long[] arr) {",
        "        for (int i = 0; i<arr.length; i++) out.print(arr[i] + \" \");",
        "        out.println();",
        "    }",
        "    public void sort(long[] a) {",
        "        shuffle(a);",
        "        Arrays.sort(a);",
        "    }",
        "",
        "    // double data-type",
        "    public double dpar() throws IOException {",
        "        return Double.parseDouble(spar());",
        "    }",
        "    public double[] dapar(int n) throws IOException {",
        "        double[] arr = new double[n];",
        "        for (int i = 0; i < n; i++) arr[i] = dpar();",
        "        return arr;",
        "    }",
        "    public static void printArray(double[] arr) {",
        "        for (int i = 0; i<arr.length; i++) out.print(arr[i] + \" \");",
        "        out.println();",
        "    }",
        "",
        "    // Generic type",
        "    public <T> void sort(T[] a) {",
        "        shuffle(a);",
        "        Arrays.sort(a);",
        "    }",
        "    public static <T> void printArray(T[] arr) {",
        "        for (int i = 0; i<arr.length; i++) out.print(arr[i] + \" \");",
        "        out.println();",
        "    }",
        "",
        "    public String spar() throws IOException {",
        "        int len = 0;",
        "        int c;",
        "        do {",
        "            c = in.read();",
        "        } while (Character.isWhitespace(c) && c != -1);",
        "        if (c == -1) {",
        "            throw new NoSuchElementException(\"Reached EOF\");",
        "        }",
        "        do {",
        "            inputBuffer[len] = (char)c;",
        "            len++;",
        "            c = in.read();",
        "        } while (!Character.isWhitespace(c) && c != -1);",
        "        while (c != '\\n' && Character.isWhitespace(c) && c != -1) {",
        "            c = in.read();",
        "        }",
        "        if (c != -1 && c != '\\n') {",
        "            in.unread(c);",
        "        }",
        "        return new String(inputBuffer, 0, len);",
        "    }",
        "",
        "    public String linepar() throws IOException {",
        "        int len = 0;",
        "        int c;",
        "        while ((c = in.read()) != '\\n' && c != -1) {",
        "            if (c == '\\r') {",
        "                continue;",
        "            }",
        "            inputBuffer[len] = (char)c;",
        "            len++;",
        "        }",
        "        return new String(inputBuffer, 0, len);",
        "    }",
        "",
        "    public boolean haspar() throws IOException {",
        "        String line = linepar();",
        "        if (line.isEmpty()) {",
        "            return false;",
        "        }",
        "        in.unread('\\n');",
        "        in.unread(line.toCharArray());",
        "        return true;",
        "    }",
        "",
        "    public void shuffle(int[] arr) {",
        "        int n = arr.length;",
        "        for (int i = 0; i < n; i++) {",
        "            int j = (int)(Math.random() * (n-i));",
        "            int temp = arr[i];",
        "            arr[i] = arr[j];",
        "            arr[j] = temp;",
        "        }",
        "    }",
        "",
        "    public void shuffle(long[] arr) {",
        "        int n = arr.length;",
        "        for (int i = 0; i < n; i++) {",
        "            int j = (int)(Math.random() * (n-i));",
        "            long temp = arr[i];",
        "            arr[i] = arr[j];",
        "            arr[j] = temp;",
        "        }",
        "    }",
        "",
        "    public void shuffle(Object[] arr) {",
        "        int n = arr.length;",
        "        for (int i = 0; i < n; i++) {",
        "            int j = (int)(Math.random() * (n-i));",
        "            Object temp = arr[i];",
        "            arr[i] = arr[j];",
        "            arr[j] = temp;",
        "        }",
        "    }",
        "",
        "    public static void main(String[] args) throws IOException {",
        "        if (FILE_INPUT) in = new PushbackReader(new BufferedReader(new FileReader(new File(\"output.txt\"))), 1 << 20);",
        "        if (FILE_OUTPUT) out = new PrintWriter(new FileWriter(new File(\"output.txt\")));",
        "",
        "        long time = 0;",
        "        time -= System.nanoTime();",
        f"        new {name}().{name}();",
        "        time += System.nanoTime();",
        "        ",
        "        if (RUN_TIMING) System.err.printf(\"%.3f ms%n\", time / 1000000.0);",
        "        ",
        "        out.flush();",
        "        in.close();",
        "    }",
        "}",
        ""
    ]
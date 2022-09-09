from collections import deque


n,m,r=map(int,input().split())

g=[[] for i in range(n)]
visited=[0]*n
pre=r
q=deque()
for i in range(m):
    a,b=map(int,input().split())
    
    


def bfs():
    while q:
        v=q.popleft()

        for i in g[v]:
            if visited[i]:
                continue
            count+=1
            visited[i]=count



       import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> now = new LinkedList<>();

        int N = sc.nextInt();
        int M = sc.nextInt();
        int R = sc.nextInt();

        int pre = R;
        int[][] nodes = new int[M][2];
        int[] node = new int[N+1];
        boolean[] node_b = new boolean[N+1];
        int i = 0;
        int c = 0;

        for (i = 0; i < M; i++) {
            nodes[i][0] = sc.nextInt();
            nodes[i][1] = sc.nextInt();
        }

        Arrays.sort(nodes, (o1, o2) -> {
            if (o1[0] == o2[0])
                return Integer.compare(o1[1], o2[1]);
            else
                return Integer.compare(o1[0], o2[0]);
        });

        for (i = 1; i <= N; i++) {
            if (nodes[i-1][0] == R) {
                now.add(nodes[i-1][1]);
                node_b[nodes[i-1][1]] = true;
                c++;
            }
        }

        node_b[R] = true;


        node[R]++;

        while (!now.isEmpty()) {
            int nn = now.poll();
            node[nn] = node[pre] + 1;
            pre = nn;
          
            for (int a = c; a < M; a++) {
                if (nodes[a][0] == nn && !node_b[nodes[a][1]]) {
                    now.add(nodes[a][1]);
                    node_b[nodes[a][1]] = true;
                }
            }
        }

        for (i = 1; i <= N; i++) {
            System.out.println(node[i]);
        }
    }
}


//[풀이 방법]
//1. bfs. 큐 만들기.
//2. 노드 개수 만큼의 배열 생성
//3. 큐가 빌 때까지 while문 진행하면서 현재 노드에 전 노드의 가중치 +1을 저장.
//4. 갔다 온 노드는 true.
//5. 배열 출력










 






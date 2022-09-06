class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.segment_tree = [0]*2*self.n
        self.lazy = [0]*2*self.n        
        self._build()   

    def query(self, start, end):
        def _query(i, j, node):
            if j < start or i > end:
                return 0
            elif i >= start and j <= end:
                return self.segment_tree[node]
            else:
                self._propagate(i, j, node)
                left_node, right_node = self._get_children(node)
                mid = (i + j) // 2            
                left = _query(i, mid, left_node)
                right = _query(mid + 1, j, right_node)
                return left + right
        return _query(0, self.n - 1, 0)

    def single_increment(self, pos, value):
        def _single_increment(i, j, node):
            if i == j:
                if i == pos:
                    self.segment_tree[node] = self.array[pos]
            else:
                mid = (i + j) // 2
                left_node, right_node = self._get_children(node)
                if pos <= mid:
                    _single_increment(i, mid, left_node)
                else:
                    _single_increment(mid + 1, j, right_node)
                self.segment_tree[node] = self.segment_tree[left_node] + self.segment_tree[right_node]
        self.array[pos] += value
        _single_increment(0, self.n - 1, 0)
    
    def increment(self, start, end, value):
        def _increment(i, j, node):
            if j < start or i > end:
                return self.segment_tree[node]
            elif i >= start and j <= end:
                self._propagate(i, j, node)
                self.segment_tree[node] += (j - i + 1) * value
                self.lazy[node] = value
                return self.segment_tree[node]
            else:
                self._propagate(i, j, node)
                left_node, right_node = self._get_children(node)
                mid = (i + j) // 2
                left = _increment(i, mid, left_node)
                right = _increment(mid + 1, j, right_node)
                self.segment_tree[node] = left + right
                return self.segment_tree[node]
        _increment(0, self.n - 1, 0)
    
    def _get_left_node(self, node):
        return node * 2 + 1

    def _get_right_node(self, node):
        return node * 2 + 2
    
    def _get_children(self, node):
        return self._get_left_node(node), self._get_right_node(node)
    
    def _build(self):
        def _build_(i, j, node):
            if i == j:
                self.segment_tree[node] = self.array[i]
            else:
                mid = (i + j) // 2
                left = _build_(i, mid, self._get_left_node(node))
                right = _build_(mid + 1, j, self._get_right_node(node))
                self.segment_tree[node] = left + right
            self.lazy[node] = float('inf')
            return self.segment_tree[node]
        _build_(0, self.n - 1, 0)
    
    def _propagate(self, i, j, node):
        if self.lazy[node] != float('inf'):
            if i != j:
                left_node, right_node = self._get_children(node)
                self.lazy[left_node] = self.lazy[node]
                mid = (i + j) // 2
                self.segment_tree[left_node] += (mid - i + 1) * self.lazy[node]
                self.lazy[right_node] = self.lazy[node]
                self.segment_tree[right_node] += (j - mid) * self.lazy[node]
            self.lazy[node] = float('inf')

    def __str__(self):
        return str(self.segment_tree) 
         

array = [1, 6, 5, 9, 8, 3, 4, 7]
st = SegmentTree(array)

print(st)

st.increment(0, 2, 1)

print(st.query(0, 2))
print(st)


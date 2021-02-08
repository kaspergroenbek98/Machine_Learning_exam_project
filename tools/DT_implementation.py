import numpy as np

class Node():
    # Initializes new node
    def __init__(self, data, min_sample_split, max_depth, node_depth):
        # Initializes attributes
        self.data = data # subset of data on Node
        self.left = None
        self.right = None
        self.class_predict = None
        self.min_sample_split = min_sample_split # Stop condition
        self.max_depth = max_depth
        self.node_depth = node_depth
        
        #print("Depth of node: ", self.node_depth)
        
        ### STOP CONDITIONS - BECOMES LEAF NODE ###
        # & then decide class (based on most frequent class in Node) 
        # If Node data length smaller than minimum sample for a leaf OR if node_depth equal to max_depth

        if (len(self.data[:,-1]) <= self.min_sample_split) or (self.node_depth == self.max_depth) or (len(set(self.data[:,-1])) == 1):
            self.counts = np.bincount(self.data[:,-1].astype(int))
            self.class_predict = np.argmax(self.counts)
            
            #print("Node ready to predict! Class:", self.class_predict)
        
        else:
            self.minimum_gini, self.minimum_gini_indexes = testGini(data, self.min_sample_split)
            self.j, self.i = self.minimum_gini_indexes[0], self.minimum_gini_indexes[1]
            self.split_value = self.data[self.j, self.i]
            self.mask = self.data[:,self.i] <= self.split_value
            self.left_data, self.right_data = self.data[self.mask], self.data[~self.mask]
            
            """print("Left data:")
            print(self.left_data)
            print("Right data:")
            print(self.right_data)
            print("\n")"""
            
        #print("true")

class DecisionTree():
    def __init__(self, min_sample_split, max_depth): 
        # Initializes empty Decision Tree
        self.root = None  # root of DT
        self.count = 0
        self.tree_depth = []
        
        # Pre-pruning
        self.min_sample_split = min_sample_split  
        self.max_depth = max_depth
    
    def insert(self, data):
        # Inserts root node or calls other function
        if not self.root:
            self.root = Node(data, self.min_sample_split, self.max_depth, 0)
            
            """print("Root data, left - right")
            print(self.root.left_data[:,-1])
            print("-")
            print(self.root.right_data[:,-1])
            print("\n")"""
            
            self.insertNode(self.root.left_data, self.root)
            self.insertNode(self.root.right_data, self.root)
        else:
            self.insertNode(data, self.root)
            
    def insertNode(self, data, node):
        #print("Inserting node", self.count)
        #print(self.depth())
        self.count += 1
        
        #print("--- TESTING ---")
        #print(node.data[:,-1])
        #print(node.class_predict)
        """print(node.left)
        print(node.right)
        print("--- ---- ---")"""
        
        """if node.class_predict:
            print("BREAAAAK")"""
        
        # Break condition if leaf node
        #if not node.class_predict:
        #if node.class_predict == -1:
        if node.class_predict is None:
            
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(node.left_data, self.min_sample_split, self.max_depth, node.node_depth+1)
                try:
                    self.insertNode(node.left.left_data, self.root) #node.left) #self.root)
                except:
                    pass
                try:
                    self.insertNode(node.left.right_data, self.root) #node.right) #self.root)
                except:
                    pass
                    
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(node.right_data, self.min_sample_split, self.max_depth, node.node_depth+1)
                try:
                    self.insertNode(node.right.left_data, self.root) #node.left) #self.root)
                except:
                    pass
                try:
                    self.insertNode(node.right.right_data, self.root) #node.right) #self.root)
                except:
                    pass
        else:
            self.tree_depth.append(node.node_depth)
            
                
    def fit(self, data):
        self.insert(data)
        
    def traverse(self, row, node):
        #print(row)
        #print(node.i)
        #if node.class_predict:
        if node.class_predict is not None:
            return node.class_predict
        else:
            if row[node.i] <= node.split_value:
                #print("value", row[node.i], "lower or equal to", node.split_value)
                return self.traverse(row, node.left)
            else:
                return self.traverse(row, node.right)
                #print("value", row[node.i], "higher than", node.split_value)
    
    
    def predict(self, data):
        predictions = []
        
        #print(len(np.shape(data)))
        
        if len(np.shape(data)) > 1:
            for row in data:
                node = self.root
                predictions.append(self.traverse(row, node))
            return np.array(predictions)
        else:
            node = self.root
            predictions.append(self.traverse(data, node))
            return np.array(predictions)

    def depth(self):
        return max(self.tree_depth)
    
    # Old depth function
    """def depth(self):
        node = self.root
        #print(node)
        return self.depthRecursive(node, depth=0)
        
    def depthRecursive(self, node, depth):
        if node.class_predict is None:
            depth += 1
            if node.left:
                return self.depthRecursive(node.left, depth)
            if node.right:
                return self.depthRecursive(node.right, depth)
        else:
            return depth """  
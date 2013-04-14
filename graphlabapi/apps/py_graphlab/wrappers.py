import cPickle;

usermod = None;

gatherEdges = 1;  # by default: gather on incoming edges
scatterEdges = 2; # by default: scatter on outgoing edges

def initUserModule(name):
	global usermod;
	usermod = __import__(name);

	global gatherEdges;
	if "gatherEdges" in dir(usermod):
		gatherEdges = usermod.gatherEdges;
	
	global scatterEdges;
	if "scatterEdges" in dir(usermod):
		scatterEdges = usermod.scatterEdges;
	return "edgeDataClass" in dir(usermod);

def newVertex():
	return usermod.vertexDataClass();

def loadVertex(vertexWrap):
	return cPickle.loads(vertexWrap);

def storeVertex(vertex):
	return cPickle.dumps(vertex);

def newEdge():
	return usermod.edgeDataClass();

def loadEdge(edgeWrap):
	return cPickle.loads(edgeWrap);

def storeEdge(edge):
	return cPickle.dumps(edge);

def newAgg():
	return usermod.aggregatorClass();

def loadAgg(aggWrap):
	return cPickle.loads(aggWrap);

def storeAgg(agg):
	return cPickle.dumps(agg);

def gatherAgg(agg1, agg2):
	agg1.merge(agg2);
	return agg1;

def transformVertex(vertex):
	return usermod.transformVertex(vertex);

def transformEdge(edge):
	return usermod.transformEdge(edge);

def saveVertex(vertex):
	return usermod.saveVertex(vertex);

def saveEdge(src, target, edge):
	return usermod.saveEdge(src, target, edge);

def gather(srcData, targetData, edgeData, numIn, numOut):
	return usermod.gather(srcData, targetData, edgeData, numIn, numOut);

def apply(targetData, agg, numIn, numOut):
	return usermod.apply(targetData, agg, numIn, numOut);

def scatter(srcData, targetData, edgeData, numIn, numOut):	
	return usermod.scatter(srcData, targetData, edgeData, numIn, numOut);
        
def parseEdge(file, line):
	return usermod.parseEdge(file, line);

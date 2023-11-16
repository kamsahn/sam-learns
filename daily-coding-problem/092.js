/*
We're given a hashmap associating each courseId key with a list of courseIds values,
which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given
{
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
},
should return ['CSC100', 'CSC200', 'CSC300'].
*/

// starting with the map, read all course ids
// if there is a course id not in the map, return null
// otherwise, comprise a set of required courses and repeat until there are no ids from the keys
// order and return

function addPrereqs(currSet, ansSet, courseMap) {
    const prerequisites = new Set();
    // convert set to array
    const currArr = Array.from(currSet);
    if (currArr.length) {
        currArr.forEach(cid => {
            // ensure course is available
            const prereqList = courseMap[cid];
            if (prereqList === undefined) {
                ansSet.add(null);
            } else {
                courseMap[cid].forEach(innerCid => {
                    prerequisites.add(innerCid);
                    ansSet.add(innerCid);
                })
            }
        })
        return addPrereqs(prerequisites, ansSet, courseMap)
    } else {
        return ansSet
    }
}

function getCourses(courseMap) {
    // get initial set of courses
    const prerequisites = new Set(Object.keys(courseMap));
    // get pre reqs
    const ansSet = addPrereqs(prerequisites, prerequisites, courseMap);
    // convert to array ans sort
    return ansSet.has(null) ? null : Array.from(ansSet).sort()
}

let courseMap = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': []
};
console.log(courseMap);
console.log("all courses are available ->", getCourses(courseMap))

courseMap = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100', 'GEO100'],
    'CSC100': []
};
console.log(courseMap);
console.log("not all courses are available ->", getCourses(courseMap))

// could make a sorter to sort by level then department 
courseMap = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100', 'GEO200'],
    'GEO200': ['CSC100', 'GEO100'],
    'GEO100': [],
    'CSC100': []
};
console.log(courseMap);
console.log("not all courses are available ->", getCourses(courseMap))
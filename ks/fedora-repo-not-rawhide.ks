repo --name=fedora --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
repo --name=updates --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=updates-released-f$releasever&arch=$basearch
#repo --name=updates-testing --mirrorlist=http://mirrors.fedoraproject.org/metalink?repo=updates-testing-f$releasever&arch=$basearch

repo --name=mesa-repo --baseurl=file:/run/media/rob/extern_data/src/mesa-on-a-stick/mesa-repo
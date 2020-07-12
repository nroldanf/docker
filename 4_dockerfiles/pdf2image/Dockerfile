FROM amazonlinux:2018.03

RUN yum -y install openjpeg-devel libjpeg-devel fontconfig-devel \
    libtiff-devel libpng-devel xz gcc gcc-c++ epel-release zip cmake3

WORKDIR "/root"

# INSTALL OpenJPEG
RUN curl -L https://github.com/uclouvain/openjpeg/archive/v2.3.1/openjpeg-2.3.1.tar.gz | tar xvz

WORKDIR "/root/openjpeg-2.3.1"

RUN mkdir -v build

WORKDIR "/root/openjpeg-2.3.1/build"

# Run cmake and return to root directory
RUN cmake3 -DCMAKE_BUILD_TYPE=Release \
            -DCMAKE_INSTALL_PREFIX=/usr \
            -DBUILD_STATIC_LIBS=OFF .. && \
            make && make install && cd ../../

# WORKDIR "/root"

# INSTALL Popler itself
RUN curl https://poppler.freedesktop.org/poppler-0.59.0.tar.xz | tar xJv && \
    cd poppler-0.59.0/ && ./configure --enable-static --enable-build-type=release && make && make install


RUN cd /root && \
    mkdir -p package/lib && \
    mkdir -p package/bin && \
    cp /usr/lib64/{libopenjpeg.so.2,libtiff.so.5,libjpeg.so.62,libpng12.so.0,libfreetype.so.6,libfontconfig.so.1,libjbig.so.2.0} /root/package/lib && \
    cp poppler-0.59.0/poppler/.libs/libpoppler.so.70 /root/package/lib && \
    cp poppler-0.59.0/utils/.libs/{pdftotext,pdfinfo,pdfseparate} /root/package/bin && \
    cd package && \
    zip -r9 ../package.zip *


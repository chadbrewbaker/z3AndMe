tar -xvf bc-1.06.tar.gz
cd bc-1.06
#http://lcamtuf.coredump.cx/afl/releases/afl-latest.tgz
afl-fuzz -i afl_in -o afl_out -x ../bc.dict -t100+ ./bc/bc @@

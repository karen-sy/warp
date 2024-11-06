#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export WARP_CACHE_PATH="$SCRIPT_DIR/warp_source_cache/"

echo "Kernel written to $WARP_CACHE_PATH"

ncu --set full --target-processes all \
    --metrics dram__bytes_read.sum,dram__bytes_written.sum,sm__inst_executed_pipe_tensor_op_hmma.avg,sm__cycles_elapsed.avg,l2_tex_read_bytes.sum,l2_tex_write_bytes.sum,lts__t_bytes.sum,lts__t_sectors_pipe_lsu_mem_rd.sum,lts__t_sectors_pipe_lsu_mem_wr.sum \
    --nvtx --call-stack \
    --export _warp_test_run -f \
    --import-source yes \
    --source-folders $WARP_CACHE_PATH \
    python test.py 
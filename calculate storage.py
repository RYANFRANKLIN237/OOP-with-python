def calculate_storage(filesize):
    block_size=4096
    full_blocks=filesize // block_size  #we use double slash to have the value with no rememnder
    partial_blocks_left_over=filesize%block_size #we use pacentage(modulo) to get just the remender
    if(partial_blocks_left_over!=0):  #!=0(is not equale to zero)
       full_blocks=full_blocks+1
       storage_size= block_size*(full_blocks+1)
       return storage_size
    else:
        storage_size=block_size*full_blocks
        return storage_size
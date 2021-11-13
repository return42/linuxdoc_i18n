/**
 * typedef sum - Sum function pointer.
 * @a: The number A.
 * @b: The number B.
 */
typedef void (*sum)(int a, int b);


/**
 * typedef genpool_algo_t: Allocation callback function type definition
 * @map: Pointer to bitmap
 * @size: The bitmap size in bits
 * @start: The bitnumber to start searching at
 * @nr: The number of zeroed bits we're looking for
 * @data: optional additional data used by the callback
 * @pool: the pool being allocated from
 */
typedef unsigned long (*genpool_algo_t)(
	unsigned long *map,
	unsigned long size,
	unsigned long start,
	unsigned int nr,
	void *data, struct gen_pool *pool,
	unsigned long start_addr);

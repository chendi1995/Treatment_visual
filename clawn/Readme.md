抓取药品时，数据有几十万，创建了一个线程池，始终容纳固定量的线程
若某一个线程超时未完成任务，则自己退出，下一个线程进来

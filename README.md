## ElasticSearch-agent

The ElasticSearch-agent is a flexible and powerful open source, collects state information by calling the ElasticSearch API
and sends it to [StatsD](https://github.com/etsy/statsd), [open-falcon](https://github.com/XiaoMi/open-falcon) etc...

### Requirements
- python (>= 2.7)
- elasticsearch (>= 2.3)


### Instructions for running the Elasticsearch agent
1. Edit `conf/settings.py` and `conf/statsd.yaml` or `conf/open-falcon.yaml` replace it with whatever you want or expand your own services
2. Agent can be started as a daemon using the following command: `python es-agent start` or `systemctl start es-agent.service`
3. The daemon can be stopped by running: `python es-agent stop` or `systemctl stop es-agent.service`
4. The daemon can be restarted by running: `python es-agent restart` or `systemctl restart es-agent.service`


### Systemd example
>\# vi /etc/systemd/system/es-agent.service



```
[Unit]
Description=Monitor agent for ElasticSearch
After=network.target

[Service]
Type=forking
WorkingDirectory=/opt/es-agent
PIDFile=/var/run/elasticsearch/es-agent.pid
ExecStart=/opt/es-agent/es-agent start
ExecReload=/opt/es-agent/es-agent restart
ExecStop=/opt/es-agent/es-agent stop
PrivateTmp=true

[Install]
WantedBy=multi-user.target

```

## 相关文档
[click me](https://github.com/RosenLo/notes/tree/master/ELK/ElasticSearch)


## 相关指标

指标 | 含义
--- | ---
es.activeprimaryshards | 集群中活跃的主分片数量
es.active_shards | 集群中活跃分片数量
es.cache.filter.evictions | field缓存里面被驱逐的数据量
es.cache.filter.size | field缓存区大小
es.cluster_status | 该es集群健康数字：红=0，黄=2，绿=1
es.docs.count | 集群中所有分片的文档
es.docs.deleted | 集群中所有分片的删除的文档
es.fielddata.evictions | fielddata缓存里面被驱逐的数据量
es.fielddata.size | fielddata缓存区大小
es.flush.total | 从开始indexflush到磁盘次数(进行一次提交并删除事务日志的操作叫做flush)
es.flush.total.time | indexflush到磁盘花费时间
es.get.current | 当前正在运行的get请求数
es.get.exists.time | 文档存在时花费在get请求上的时间
es.get.exists.total | 文档存在时get请求次数
es.get.missing.time | 文档丢失时花费在get请求上的时间
es.get.missing.total | 文档丢失时get请求次数
es.get.time | 花费在get请求上的总时间
es.get.total | 总的get请求次数
es.http.current_open | 当前打开的http连接数
es.http.total_opened | 打开http的总连接数
es.id_cache.sizeid | 缓存的大小
es.indexing.delete.current | 当前从一个index中删除的文档数量
es.indexing.delete.time | 从一个index中删除文档花费的总时间
es.indexing.delete.total | 从一个index中删除的文档数量
es.indexing.index.current | 当前一个index中被索引的文档数量
es.indexing.index.time | 从一个index索引文档所花费的时间
es.indexing.index.total | 一个index中被索引的文档数量
es.initializing_shards | 当前初始化碎片数量
es.merges.current | 当前的活跃段合并数量
es.merges.current.docs | 当前跨段合并的文档数量
es.merges.current.size | 当前被合并的段的大小
es.merges.total | 所有段的合并数量
es.merges.total.docs | 跨所有合并段的文档数量
es.merges.total.size | 所有合并段的大小
es.merges.total.time | 花在合并段上的时间
es.numberofnodes | 集群中node总数
es.pendingtaskspriority_high | 高优先级的未完成的task数量
es.pendingtaskspriority_urgent | 紧急优先未完成的task数量
es.pendingtaskstotal | 总的未完成的task数量
es.primaries.docs.count | 主分片上的文档总量
es.primaries.docs.deleted | 主分片上删除的文档总量
es.primaries.flush.total | 主分片上从开始时间indexflush到磁盘次数
es.primaries.flush.total.time | 主分片上indexflush到磁盘花费时间
es.primaries.get.current | 主分片上当前正在运行的get请求数
es.primaries.get.exists.time | 主分片上文档存在时花费在get请求上的时间
es.primaries.get.exists.total | 主分片上文档存在时get请求次数
es.primaries.get.missing.time | 主分片上文档丢失时花费在get请求上的时间
es.primaries.get.missing.total | 主分片上文档丢失时get请求次数
es.primaries.get.time | 主分片上花费在get请求上的总时间
es.primaries.get.total | 主分片上总的get请求次数
es.primaries.indexing.delete.current | 主分片上当前从一个index中删除的文档数量
es.primaries.indexing.delete.time | 主分片上从一个index中删除文档花费的总时间
es.primaries.indexing.delete.total | 主分片上从一个index中删除的文档数量
es.primaries.indexing.index.current | 主分片上当前一个index中被索引的文档数量
es.primaries.indexing.index.time | 主分片上从一个index索引文档所花费的时间
es.primaries.indexing.index.total | 主分片上一个index中被索引的文档数量
es.primaries.merges.current | 主分片上当前的活跃段合并数量
es.primaries.merges.current.docs | 主分片上当前跨段合并的文档数量
es.primaries.merges.current.size | 主分片上当前被合并的段的大小
es.primaries.merges.total | 主分片上所有段的合并数量
es.primaries.merges.total.docs | 主分片上跨所有合并段的文档数量
es.primaries.merges.total.size | 主分片上所有合并段的大小
es.primaries.merges.total.time | 主分片上花在合并段上的时间
es.primaries.refresh.total | 主分片上index刷新总数量
es.primaries.refresh.total.time | 主分片上index刷新花费的总时间
es.primaries.search.fetch.current | 当前运行在主分片上查询取回操作的数量
es.primaries.search.fetch.time | 在主分片上查询取回操作的总时间
es.primaries.search.fetch.total | 在主分片上查询取回操作的数量
es.primaries.search.query.current | 当前运行在主分片上查询操作的数量
es.primaries.search.query.time | 在主分片上查询操作的总时间
es.primaries.search.query.total | 在主分片上查询操作的数量
es.primaries.store.size | 所有主分片的大小/bytes
es.process.open_fd | 打开和当前进程相关的文件数据，如果不是－1
es.refresh.total | 总的index刷新次数
es.refresh.total.time | 总的index刷新花费的时间
es.relocating_shards | 从一个节点搬到另一个节点的分片数量
es.search.fetch.current | 当前运行的查询取回操作的数量
es.search.fetch.open_contexts | 活跃查询次数
es.search.fetch.time | 查询取回操作的总时间
es.search.fetch.total | 查询取回操作的数量
es.search.query.current | 当前运行查询操作的数量
es.search.query.time | 查询操作的总时间
es.search.query.total | 查询操作的数量
es.store.size | 总的存储大小/bytes
es.thread_pool.bulk.active | 在bulk线程池活跃的线程数
es.thread_pool.bulk.queue | 在bulk线程池排队的线程数
es.thread_pool.bulk.threads | 在bulk线程池总的线程数
es.thread_pool.flush.active | 在flush队列中活跃的线程数
es.thread_pool.flush.queue | 在flush线程池排队的线程数
es.thread_pool.flush.threads | 在flush线程池总的线程数
es.thread_pool.generic.active | 在generic线程池活跃的线程数
es.thread_pool.generic.queue | 在generic线程池排队的线程数
es.thread_pool.generic.threads | 在generic线程池总的线程数
es.thread_pool.get.active | 在get线程池活跃的线程数
es.thread_pool.get.queue | 在get线程池排队的线程数
es.thread_pool.get.threads | 在get线程池总的线程数
es.thread_pool.index.active | 在index线程池活跃的线程数
es.thread_pool.index.queue | 在index线程池排队的线程数
es.thread_pool.index.threads | 在index线程池总的线程数
es.thread_pool.management.active | 在management线程池活跃的线程数
es.thread_pool.management.queue | 在management线程池排队的线程数
es.thread_pool.management.threads | 在management线程池总的线程数
es.thread_pool.merge.active | 在merge线程池活跃的线程数
es.thread_pool.merge.queue | 在merge线程池活跃的排队数
es.thread_pool.merge.threads | 在merge线程池总的线程数
es.thread_pool.percolate.active | 在percolate线程池活跃的线程数
es.thread_pool.percolate.queue | 在percolate线程池排队的线程数
es.thread_pool.percolate.threads | 在percolate线程池总的线程数
es.thread_pool.refresh.active | 在refresh线程池活跃的线程数
es.thread_pool.refresh.queue | 在refresh线程池排队的线程数
es.thread_pool.refresh.threads | 在refresh线程池总的线程数
es.thread_pool.search.active | 在search线程池活跃的线程数
es.thread_pool.search.queue | 在search线程池排队的线程数
es.thread_pool.search.threads | 在search线程池总的线程数
es.thread_pool.snapshot.active | 在snapshot线程池活跃的线程数
es.thread_pool.snapshot.queue | 在snapshot线程池排队的线程数
es.thread_pool.snapshot.threadsv | 在snapshot线程池总的线程数
es.transport.rx_count | 在集群通信中接受的包的总数量
es.transport.rx_size | 在集群通信中接受的数据大小/bytes
es.transport.server_open | 为集群通信打开的连接数
es.transport.tx_count | 在集群通信中发送的包的总数量
es.transport.tx_size | 在集群通信中发送的数据大小/bytes
es.unassigned_shards | 那些未分配节点的分片数量
es.jvm.mem.non_heap_user_in_btyes | 加载类使用的大小

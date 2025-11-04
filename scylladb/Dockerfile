FROM scylladb/scylla-manager-agent:3.4.2 AS agent
FROM scylladb/scylla:5.4.2

COPY --from=agent /usr/bin/scylla-manager-agent /usr/bin/
#include <iostream>
#include <list>
#include <unordered_map>

struct Node
{
    int val;
    std::list<int>::iterator it; // key在LRU链表中的位置
};

class LFUCache
{
private:
    // 键-值索引表
    // {key1:(val1,list_it1),
    //  key2:(val2,list_it2),
    //  ...}
    std::unordered_map<int, Node> m_key2val;

    // 键值-频次索引表
    // {key1:freq1,
    //  key2:freq2,
    //  ...}
    std::unordered_map<int, int> m_key2freq;

    // 频次-key的LRU链表，双向链表表头为最近使用的key，表尾为最久未使用的key
    std::unordered_map<int, std::list<int>> m_freq2list;

    int m_lowest_freq; // 最低次数
    int m_cap;         // 容量

public:
    LFUCache(int capacity)
    {
        this->m_cap = capacity;
        this->m_lowest_freq = 0;
    }

    int get(int key)
    {
        if (this->m_key2val.find(key) == this->m_key2val.end() || this->m_cap <= 0)
        {
            return -1;
        }

        put(key, this->m_key2val.at(key).val);
        return this->m_key2val.at(key).val;
    }

    void put(int key, int val)
    {
        if (this->m_cap <= 0)
        {
            return;
        }
        // 若键值不存在
        if (this->m_key2val.find(key) == this->m_key2val.end())
        {
            // 若容量已满，需要删除使用次数最少的键
            if (this->m_key2val.size() == this->m_cap)
            {
                // 最低频次且时间最早的键
                int key_need_del = this->m_freq2list.at(this->m_lowest_freq).back();
                this->m_freq2list.at(this->m_lowest_freq).pop_back();
                if (this->m_freq2list.at(this->m_lowest_freq).empty())
                {
                    this->m_freq2list.erase(this->m_lowest_freq);
                }

                this->m_key2val.erase(key_need_del);
                this->m_key2freq.erase(key_need_del);
            }

            // 新增数据
            this->m_lowest_freq = 1;              // 最低频次
            this->m_key2freq[key] = 1;            // 频次索引表
            this->m_freq2list[1].push_front(key); // 新键插在链表头部
            this->m_key2val[key].val = val;       // 键值索引表
            this->m_key2val.at(key).it = this->m_freq2list.at(1).begin();
        }
        // 键值存在则更新
        else
        {
            int key_freq = this->m_key2freq.at(key);                          // 键值的使用次数
            this->m_freq2list.at(key_freq).erase(this->m_key2val.at(key).it); // 使用次数增加，从双向链表中删除
            if (this->m_freq2list.at(key_freq).empty())
            { // 如果当前频次的双向链表为空
                if (this->m_lowest_freq == key_freq)
                {
                    this->m_lowest_freq++;
                }
                this->m_freq2list.erase(key_freq);
            }

            key_freq++;
            this->m_key2freq.at(key) = key_freq;
            this->m_freq2list[key_freq].push_front(key); // 加入链表
            this->m_key2val[key].val = val;
            this->m_key2val[key].it = this->m_freq2list.at(key_freq).begin();
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
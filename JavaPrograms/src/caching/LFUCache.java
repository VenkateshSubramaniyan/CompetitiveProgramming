package caching;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

// https://www.enjoyalgorithms.com/blog/least-frequently-used-cache
public class LFUCache {

    private Map<Integer, Node> valueMap = new HashMap<>();

    private Map<Integer, Integer> countMap = new HashMap<>();

    private TreeMap<Integer, DoublyLinkedList> frequencyMap = new TreeMap<>();

    private final int size;

    public LFUCache(int size) {
        this.size = size;
    }

    public int get(int key) {
        if (!valueMap.containsKey(key) || size == 0) {
            return -1;
        }

        // Remove element from the curent freq list and move it to the next one in O(1) time
        Node nodeToDelete = valueMap.get(key);
        Node node = new Node(key, nodeToDelete.value);
        int frequency = countMap.get(key);
        removeIfListEmpty(frequency);
        valueMap.remove(key);
        countMap.remove(key);
        valueMap.put(key, node);
        countMap.put(key, frequency + 1);
        frequencyMap.computeIfAbsent(frequency + 1, k -> new DoublyLinkedList()).add(node);
        return valueMap.get(key).value;

    }

    public void put(int key, int value) {

        if (!valueMap.containsKey(key) && size > 0) {
            Node node = new Node(key, value);
            if (valueMap.size() == size) {
                int lowestCount = frequencyMap.firstKey();
                Node nodeTodelete = frequencyMap.get(lowestCount).getHead();
                removeIfListEmpty((lowestCount));

                int keyToDelete = nodeTodelete.getKey();
                valueMap.remove(keyToDelete);
                countMap.remove(keyToDelete);
            }
            frequencyMap.computeIfAbsent(1, k -> new DoublyLinkedList()).add(node);
            valueMap.put(key, node);
            countMap.put(key, 1);

        } else if (size > 0) {
            Node node = new Node(key, value);
            Node nodeToDelete = valueMap.get(key);
            int frequency = countMap.get(key);
            frequencyMap.get(frequency).remove(nodeToDelete);
            removeIfListEmpty(frequency);

            valueMap.remove(key);
            countMap.remove(key);
            valueMap.put(key, node);
            countMap.put(key, frequency + 1);
            frequencyMap.computeIfAbsent(frequency + 1, k -> new DoublyLinkedList()).add(node);

        }
    }

    private void removeIfListEmpty(int frequency) {
        // remove from map if list is empty
        if (frequencyMap.get(frequency).size() == 0) {
            frequencyMap.remove(frequency);
        }

    }


    private class Node {

        private int key;
        private int value;
        private Node next;
        private Node prev;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }

        public int getKey() {
            return key;
        }

        private int getValue() {
            return value;
        }


    }


    private class DoublyLinkedList {
        private int n;
        private Node head;
        private Node tail;

        public void add(Node node) {
            if (head == null) {
                head = node;
            } else {
                tail.next = node;
                tail.prev = tail;
            }
            tail = node;
            n++;
        }

        public void remove(Node node) {
            if (node.next == null) tail = node.prev;
            else node.next.prev = node.prev;

            if (node.prev == null) head = node.next;
            else node.prev.next = node.next;

            n--;
        }

        public Node getHead() {
            return head;
        }

        public int size() {
            return n;
        }


    }

}

